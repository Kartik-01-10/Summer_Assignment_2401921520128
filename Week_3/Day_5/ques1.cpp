class MyQueue {
public:
    stack<int> st;
    MyQueue() { 
    }
    void push(int x) {
        if(st.empty()){
            st.push(x);
            return;
        }
        vector<int>v; 
        while(!st.empty()){
            v.push_back(st.top());
            st.pop();
        }
        st.push(x);
        for (int i = v.size()-1; i>= 0 ; i--){
            st.push(v[i]);
        }
    }
    
    int pop() {
        int x = st.top();
        st.pop();
        return x;
    }
    
    int peek() {
        return st.top();
    }
    
    bool empty() {
        return st.empty();
    }
};

