:-include(dataHorari).

showData:- horari(A,G,D,H), write(A),write(','),write(G),write(','),write(D),write(','),
write(H),nl,fail.
showData.
getData(L):- findall([A,G,D,H],horari(A,G,D,H),L).

solution:-findall([A,G,D,H],horari(A,G,D,H),L),retractall(horarioF(_)),assert(horarioF([])),
  trobaHorari(L),horarioF(Sol),tell(horari),displaySol(Sol),told.
solution.
displaySol([]).
displaySol([[A,G,D,H]|L]):- write(A),write(','),write(G),write(','),write(D),write(','),
write(H),nl,displaySol(L).

trobaHorari([]).
trobaHorari([[A,G,D,H]|L]):-trobaHorari(L),
  \+horaOcupada(D,H),retract(horarioF(AH)),
  assert(horarioF([[A,G,D,H]|AH])).
trobaHorari(_).

horaOcupada(D,H) :- horarioF(L),member([_,_,D,H],L).

test:-testAux,write('k'),fail.
testAux:-write('why').
testAux:-write('xx'),nl.

main:- solution,halt.