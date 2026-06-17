class MinStack {
public:
    stack<int> st, helper;

    MinStack() {}

    void push(int val) {
        st.push(val);
        if (helper.empty() || val <= helper.top()) {
            helper.push(val);
        }
    }

    void pop() {
        if (st.top() == helper.top()) {
            helper.pop();
        }
        st.pop();
    }

    int top() {
        return st.top();
    }

    int getMin() {
        return helper.top();
    }
};
