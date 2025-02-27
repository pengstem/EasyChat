#include <iostream>
#include <cmath>
#include <stack>
#include <string>
#include <vector>

using namespace std;

// Function to determine operator precedence
int precedence(char op) {
    if (op == '+' || op == '-')
        return 1;
    if (op == '*' || op == '/')
        return 2;
    if (op == '^')
        return 3;
    return 0;
}

long long computer(string s){
    vector<long long> nums;
    vector<char> postfix;
    stack<char> operators;
    
    // Handle unary minus at the beginning
    if(s[0]=='-') s="0"+s;
    
    for(int i=0; i<s.size(); i++){
        if(s[i]==' ') continue;
        
        if(s[i]>='0' && s[i]<='9'){
            long long num=0;
            while(i<s.size() && s[i]>='0' && s[i]<='9'){
                num = num*10 + (s[i]-'0');
                i++;
            }
            nums.push_back(num);
            i--; // Step back as loop will increment i
            postfix.push_back('n'); // Mark as number
        }
        else if(s[i]=='(') {
            operators.push(s[i]);
        }
        else if(s[i]==')'){
            while(!operators.empty() && operators.top()!='('){
                postfix.push_back(operators.top());
                operators.pop();
            }
            if(!operators.empty()) // Pop the '('
                operators.pop();
        }
        else if(s[i]=='+' || s[i]=='-' || s[i]=='*' || s[i]=='/' || s[i]=='^'){
            while(!operators.empty() && operators.top()!='(' && 
                  precedence(operators.top()) >= precedence(s[i])){
                postfix.push_back(operators.top());
                operators.pop();
            }
            operators.push(s[i]);
        }
    }
    
    while(!operators.empty()){
        postfix.push_back(operators.top());
        operators.pop();
    }
    
    stack<long long> evaluation;
    int numIndex = 0;
    
    for(char token : postfix){
        if(token == 'n'){
            evaluation.push(nums[numIndex++]);
        } else {
            if(evaluation.size() < 2){
                cout << "Error: Invalid expression" << endl;
                return 0;
            }
            
            long long b = evaluation.top();
            evaluation.pop();
            long long a = evaluation.top();
            evaluation.pop();
            
            switch(token){
                case '+': evaluation.push(a+b); break;
                case '-': evaluation.push(a-b); break;
                case '*': evaluation.push(a*b); break;
                case '/': 
                    if(b == 0){
                        cout << "Error: Division by zero" << endl;
                        return 0;
                    }
                    evaluation.push(a/b); 
                    break;
                case '^': evaluation.push(pow(a,b)); break;
            }
        }
    }
    
    if(evaluation.empty()){
        cout << "Error: Invalid expression" << endl;
        return 0;
    }
    
    return evaluation.top();
}

int main(){
    cout << "Enter the expression: ";
    string s;
    getline(cin,s);
    cout << computer(s) << endl;
    return 0;
}