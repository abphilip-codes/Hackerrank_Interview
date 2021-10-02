// https://www.hackerrank.com/challenges/crossword-puzzle/problem

#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'crosswordPuzzle' function below.
 *
 * The function is expected to return a STRING_ARRAY.
 * The function accepts following parameters:
 *  1. STRING_ARRAY crossword
 *  2. STRING words
 */

bool crosswordPuzzle(vector<string>& crossword, vector<string>& words) {
    auto try_place = [&](auto i, auto j, auto r) {
        auto word = words.back();
        if ((r?j:i)+word.length() > 10) return false;
        for (size_t k = 0; k < word.length(); ++k) {
            if (crossword[r?i:i+k][r?j+k:j] != '-' 
             && crossword[r?i:i+k][r?j+k:j] != word[k])
                return false;
        }                
        auto crossword_copy = crossword;
        for (size_t k = 0; k < word.length(); ++k)
            crossword[r?i:i+k][r?j+k:j] = word[k];
        words.pop_back();
        bool success = crosswordPuzzle(crossword, words);
        words.push_back(word);
        if (!success) crossword = crossword_copy;
        return success;
    };
    if (words.size() == 0) return true;
    for (size_t i = 0; i < 10; ++i) {
        for (size_t j = 0; j < 10; ++j) {
            if (try_place(i, j, 1/*by row*/)) return true;
            if (try_place(i, j, 0/*by col*/)) return true;
        }
    }
    return false;
};

vector<string> crosswordPuzzle(vector<string> crossword, string words) {
    vector<string> word_vec;
    for (size_t i = 0, j = 0; i < words.length(); ++i) {
        if (words[i] == ';') {
            word_vec.push_back(words.substr(j, i-j));
            j = i+1;
        } else if (i == words.length()-1)
            word_vec.push_back(words.substr(j, i-j+1));
    }
    crosswordPuzzle(crossword, word_vec);
    return crossword;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    vector<string> crossword(10);

    for (int i = 0; i < 10; i++) {
        string crossword_item;
        getline(cin, crossword_item);

        crossword[i] = crossword_item;
    }

    string words;
    getline(cin, words);

    vector<string> result = crosswordPuzzle(crossword, words);

    for (size_t i = 0; i < result.size(); i++) {
        fout << result[i];

        if (i != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}