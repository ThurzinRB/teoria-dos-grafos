#include <iostream>

using namespace std;

int main(int arc, const char** argv){

    cout<<"hello world\n";
    int n;
    int l;
    cin>>n;
    cin>>l;

    cout<<"Valor de n: "<<n<<" Valor de l: "<< l<< "\n";

    string s;
    
    while (getline(cin, s) && !s.empty()) {
        cout<<"hello world\n";
    }

    return 0;
}