#include<bits/stdc++.h>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
#define int long long
using namespace std;
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
typedef tree<int, null_type, less_equal<int>, rb_tree_tag, tree_order_statistics_node_update> oset;
template<typename T> bool smin(T& a, const T& b) { if (b < a) { a = b; return true; } return false;}
template<typename T> bool smax(T& a, const T& b) { if (a < b) { a = b; return true; } return false;}
template <class A, class B> ostream &operator<<(ostream &out, const pair<A, B> &a){return out << a.first << " " << a.second;}
template<typename T> istream &operator>>(istream &in, vector<T> &v) { for (auto &x: v) in >> x; return in; }
template<typename T> ostream &operator<<(ostream &out, const vector<T> &v) { for (const T &x: v) out << x << ' ';return out;}
template <class K, class V> using ht = gp_hash_table<K, V, hash<K>, equal_to<K>, direct_mask_range_hashing<>, linear_probe_fn<>, hash_standard_resize_policy<hash_exponential_size_policy<>, hash_load_check_resize_trigger<>, true>>;
#ifndef ONLINE_JUDGE
#define dout(...) cerr << "Line:" << __LINE__ << " [" << #__VA_ARGS__ << "] = ["; _print(__VA_ARGS__)
#else
#define dout(...)
#endif
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
inline int gen_random(int l, int r) {
    return uniform_int_distribution<int>(l, r)(rng);
}
void pbit(int a) {
    cout << a << " : " << bitset<40>(a) << endl;
}
auto setIO = [](string name = "") {
    ios_base::sync_with_stdio(0);
    cin.tie(0);  cout.tie(0);
    if (!name.empty()) {
        freopen((name + ".in").c_str(), "r", stdin);
        freopen((name + ".out").c_str(), "w", stdout);
    }
    return 0;
}();
void Solve() {
    int n;
    cin >> n;

    vector<int> a(n), b(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i] >> b[i];
    }

    function<bool(int)> f = [&](int target) -> bool {
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (target - 1 - a[i] <= cnt and cnt <= b[i]) {
                cnt++;
            }
        }
        return cnt >= target;
    };

    int l = 1, r = n, ans = 1;
    while (l <= r) {
        int mid = (l + r) >> 1;

        if (f(mid)) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    cout << ans;
}
int32_t main() {
    int tc;
    cin >> tc;

    for (int i = 1; i <= tc; i++) {
        if (i != 1) {
            cout << endl;
        }
        //cout << "Case "<< i << ": ";
        Solve();
    }
    return 0;
}
