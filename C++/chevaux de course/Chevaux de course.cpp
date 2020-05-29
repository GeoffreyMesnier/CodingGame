#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
    int limiteBasse;
    int limiteHaute;
    int N;
    cin >> N; cin.ignore();
    int difMin = 0;
    int dif = 0;
    int tabPui[N];
    //Recupere les valeurs des puissances
    for (int i = 0; i < N; i++) {
        int Pi;
        cin >> Pi; cin.ignore();
        tabPui[i] = Pi;
    }

    sort(tabPui,tabPui+N);
    //Parcours les différentes valeur pour trouver la plus proche
    for (int j=0; j<N; j++){
            dif = abs(tabPui[j] - tabPui[j+1]);
            if (difMin == 0 and dif != 0)
            {
                difMin= dif;
            }
            else if ((dif < difMin) and (dif != 0))
            {
                difMin = dif;
            }
    }
    
    // Affiche le resultat
    cout << difMin << endl;
}
