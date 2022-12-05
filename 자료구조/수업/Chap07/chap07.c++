template<class ItemType>
void QuickSort(ItemType value[], int first, int last)
{
// Pre : first <= last
// post: Sorts array values[first. .last] into
// ascending order

    if (first < last)
    {
        int splitPoint;
        Split(value, first, last, splitPoint);

        QuickSort(value, first, splitPoint - 1);
        QuickSort(value, splitPoint + 1, last);
    }
}