from mimetypes import init
import pyupbit
import pandas as pd
import numpy


Path = "C:\\Coding\\kyunghee\\소프트웨어융합개론\\File\\coin_ohlcv\\"
file_root = (Path+"{0}.xlsx".format("KRW-BTC"))
readed_excel = pd.read_excel(file_root)
data_np = pd.DataFrame.to_numpy(readed_excel)

# 기본적인 여러가지 식에 대해 정의하는 함수
def The_define(open, close, high, low):
    if open >= close:
        big = open
        small = close
    else:
        big = close
        small = open
    # 고가와 저가의 차이
    full = high - low
    full_len = abs(full)
    # 시가와 저가의 차이(코인장은 9:00시부터 8:59시 까지 진행된다.)
    result = close - open
    result_len = abs(result)
    # 하루 동안의 한 티커의 상승/하락률
    percent = result/open
    percent_len = abs(percent)
    # day_result의 중심값
    result_center = (open+close)/2
    # full의 중심값
    full_center = (high+low)/2

    # 전체 중앙 값에서 부터 최고, 최저가까지의 거리
    # 절대값으로 나옴
    half_len = high - full_center

    # day_result의 중앙값으로부터 최고, 최저가까지의
    # 절대값으로 나옴
    result_high = abs(high - result_center)
    result_low = abs(result_center - low)

    # 둘중에 더 큰 값을 big 작은 값을 small로 정의함.
    if result_high >= result_low:
        result_big = result_high
        result_small = result_low
    elif result_high < result_low:
        result_big = result_low
        result_small = result_high

    return big, small, full, full_len, result, result_len, percent, percent_len, result_center, full_center, half_len, result_high, result_low, result_big, result_small


# (시가/종가)와 (최고/최저가) 사이의 거리를 계산하는 함수
def The_Detail(open, close, high, low):

    if open >= close:
        high_range = (high - open)
        low_range = (close-low)
    elif open < close:
        high_range = (high - close)
        low_range = (open-low)

    if high_range < low_range:
        range_big = low_range
        range_small = high_range
    elif high_range >= low_range:
        range_big = high_range
        range_small = low_range

    return high_range, low_range, range_big, range_small


# 상승장 하락장 분석 함수
def The_UpDown(open, close):
    if open < close:
        the_result = "상승장"
    else:
        the_result = "하락장"
    return the_result


def analysis_main():
    # 엑셀의 값 가져오기
    # 배열 [가로값][세로값]
    for i in range(500):
        today_date = data_np[i][0]
        day_open = data_np[i][1]
        day_close = data_np[i][4]
        day_high = data_np[i][2]
        day_low = data_np[i][3]

        today_result = The_UpDown(day_open, day_close)
        # 함수로부터 가져오기
        day_big, day_small, day_full, day_full_len, day_result, day_result_len, day_percent, day_percent_len, day_result_center, day_full_center, day_half_len, day_result_high, day_result_low, day_result_big, day_result_small = The_define(
            day_open, day_close, day_high, day_low)

        # day_result로 부터 얼마나 떨어져있는지 길이를 알아보기 위한 함수와 명명
        # 절대값으로 결과값이 나옴
        day_high_range, day_low_range, day_range_big, day_range_small = The_Detail(
            day_open, day_close, day_high, day_low)

        # 퍼센트의 세분화
# ------------------------------------------------------------------------------------------#
        # 0% ~ 1.25%: 매우 작음
        if 0 <= abs(day_percent) <= 0.0125:
            # day_close와 day_open의 가격이 각각 하한가와 상한가와 1.5%미만으로 변동시 이를 작은 십자가형으로 명명한다.
            if day_result_big < 0.02:
                print("포프라이트")
            elif 0.02 <= day_result_big <= 0.11:
                if day_result_big*(0.5) > day_result_small:
                    print("잠자리형")
                else:
                    print("작은 크기의 잠자리")
            elif day_result_big > 0.11:
                print('스트라이트: {0}/{1}'.format(today_result, today_date))

# ------------------------------------------------------------------------------------------#
        # 1.25% ~ 4%: 작음
        elif 0.0125 < abs(day_percent) <= 0.04:
            # 평범한 캔들
            if day_half_len > day_range_big:
                # 전체 움직임에 3/4이상 일 경우 꽉찬 캔들/ 이하일 경우 꽉차지 않은 캔들
                if (day_full_len*(0.7)) > day_result_len:
                    print('꽉차지 않은 작은 캔들: {0}/{1}'.format(today_result, today_date))
                else:
                    print('꽉찬 작은 캔들: {0}/{1}'.format(today_result, today_date))

            # 망치형
            elif day_half_len <= day_range_big:
                # 중심부로부터 가장 낮은 값이
                if day_small >= day_full_center:
                    print('윗망치 작은 캔들: {0}/{1}'.format(today_result, today_date))
                elif day_big < day_full_center:
                    print('아래망치 작은 캔들: {0}/{1}'.format(today_result, today_date))
                else:
                    print("버그값?")

# ------------------------------------------------------------------------------------------#
        # 4% ~ 7%: 일반(작음)
        elif 0.04 < abs(day_percent) <= 0.07:
            # 평범한 캔들
            if day_half_len > day_range_big:
                # 전체 움직임에 3/4이상 일 경우 꽉찬 캔들/ 이하일 경우 꽉차지 않은 캔들
                if (day_full*(0.7)) > day_result_len:
                    print('꽉차지 않은 일반(작은) 캔들: {0}/{1}'.format(today_result, today_date))
                else:
                    print('꽉찬 일반(작은) 캔들: {0}/{1}'.format(today_result, today_date))

            # 망치형
            elif day_half_len <= day_range_big:
                # 중심부로부터 가장 낮은 값이
                if day_small >= day_full_center:
                    print('윗망치 일반(작은) 캔들: {0}/{1}'.format(today_result, today_date))
                elif day_big < day_full_center:
                    print('아래망치 일반(작은) 캔들: {0}/{1}'.format(today_result, today_date))
                else:
                    print("버그값?")


# ------------------------------------------------------------------------------------------#
        # 7% ~ 15%: 일반(큼)
        elif 0.07 < abs(day_percent) <= 0.15:
            # 평범한 캔들
            if day_half_len > day_range_big:
                # 전체 움직임에 3/4이상 일 경우 꽉찬 캔들/ 이하일 경우 꽉차지 않은 캔들
                if (day_full*(0.7)) > day_result_len:
                    print('꽉차지 않은 일반(큰) 캔들: {0}/{1}'.format(today_result, today_date))
                else:
                    print('꽉찬 일반(큰) 캔들: {0}/{1}'.format(today_result, today_date))

            # 망치형
            elif day_half_len <= day_range_big:
                # 중심부로부터 가장 낮은 값이
                if day_small >= day_full_center:
                    print('윗망치 일반(큰) 캔들: {0}/{1}'.format(today_result, today_date))
                elif day_big < day_full_center:
                    print('아래망치 일반(큰) 캔들: {0}/{1}'.format(today_result, today_date))
                else:
                    print("버그값?")

# ------------------------------------------------------------------------------------------#
        # 15% ~ 25%: 큼
        elif 0.15 < abs(day_percent) <= 0.025:
            # 평범한 캔들
            if day_half_len > day_range_big:
                # 전체 움직임에 3/4이상 일 경우 꽉찬 캔들/ 이하일 경우 꽉차지 않은 캔들
                if (day_full*(0.7)) > day_result_len:
                    print('꽉차지 않은 큰 캔들: {0}/{1}'.format(today_result, today_date))
                else:
                    print('꽉찬 큰 캔들: {0}/{1}'.format(today_result, today_date))

            # 망치형
            elif day_half_len <= day_range_big:
                # 중심부로부터 가장 낮은 값이
                if day_small >= day_full_center:
                    print('윗망치 큰 캔들: {0}/{1}'.format(today_result, today_date))
                elif day_big < day_full_center:
                    print('아래망치 큰 캔들: {0}/{1}'.format(today_result, today_date))
                else:
                    print("버그값?")

# ------------------------------------------------------------------------------------------#
        # 25%~ : 매우 큼
        elif abs(day_percent) > 0.25:
            print('오버 슈팅: {0}/{1}'.format(today_result, today_date))


def main():
    analysis_main()
    
main()