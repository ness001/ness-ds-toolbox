void dfs(int pos, string s, int n)
{
	if (pos == n)
	{
		if(s != "") cout << s << endl;
		return;
	}
	for (int i = 0; i <= 9; i++)
	{
		if(s != "" || (s == "" && i != 0)) s += to_string(i);
		dfs(pos + 1,s,n);
		s = s.substr(0, s.size()-1);
	}
}

int main()
{
	int n;
	cin >> n;
	string s = "";
	bfs(0, s, n);
	system("pause");
	return 0;
}