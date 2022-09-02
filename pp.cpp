#include <bits/stdc++.h>
#include <string.h>

typedef long long ll;

using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        ll n;
        cin >> n;
        if (n % 3 == 0)
        {
            cout << (n / ll(3))<<endl;
            continue;
        }

        if(n==4)
        {
            cout<<2<<endl;
            continue;
        }

        if(n==1)
        {
            cout<<2<<endl;
            continue;
        }

        if (n % 3 == 1 && n!=4)
        {
            ll ans = ((n-ll(4)) / ll(3)) + ll(2);
            cout << ans<<endl;
            continue;
        }

        //if(n%3==2)
        else
        {
            ll ans = (n / ll(3)) + ll(1);
            cout << ans<<endl;
            continue;
        }

       // cout << endl;
    }

    return 0;
}