#include <iostream>
#include <sstream>
#include <vector>
#include <string>
using namespace std;

struct qorld_cup
{
	qorld_cup(vector <string> team_names)
	{
		// TODO
	}

	void add_game_result(string team_name1, int goals1, int cards1, string team_name2, int goals2, int cards2)
	{
		// TODO
	}

	int get_score(string team_name)
	{
		// TODO
		return 0;
	}

	int get_rank(string team_name)
	{
		// TODO
		return 0;
	}
};

int main()
{
	int n = 32;
	int q;
	cin >> q;
	vector <string> team_names;
	for(int i = 0; i < n; i++)
	{
		string team_name;
		cin >> team_name;
		team_names.push_back(team_name);
	}
	qorld_cup qc(team_names);
	string order;
	cin.ignore();
	for(int i = 0; i < q; i++)
	{
		getline(cin, order);
		stringstream ss(order);
		string type;
		ss >> type;
		if(type == "add_game_result")
		{
			string team_name1, team_name2;
			int goals1, goals2, cards1, cards2;
			ss >> team_name1 >> goals1 >> cards1 >> team_name2 >> goals2 >> cards2;
			qc.add_game_result(team_name1, goals1, cards1, team_name2, goals2, cards2);
		}
		if(type == "get_rank")
		{
			string team_name;
			ss >> team_name;
			cout << qc.get_rank(team_name) << endl;
		}
		if(type == "get_score")
		{
			string team_name;
			ss >> team_name;
			cout << qc.get_score(team_name) << endl;
		}
	}
}
