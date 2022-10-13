#include "StackType.h"

int main() {
	StackType st;
	for (int i = 0; i < 20; i++) {
		st.Push(i);
	}
	st.Print();
	StackType st2;
	// st.Copy(st2);
	st2 = st;
	st2.Print();
	st.Pop();
	st.Pop();
	st.Pop();
	st.Print();
	st2.Print();
}
