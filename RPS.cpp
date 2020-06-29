#include <iostream>
#include <stdlib.h>

int main(){
  srand (time(NULL));
  int computer = rand() % 3 + 1;
  int user = 0;

  std::cout << "====================\n";
  std::cout << "rock paper scissors!\n";
  std::cout << "====================\n";

  std::cout << "1) ✊\n";
  std::cout << "2) ✋\n";
  std::cout << "3) ✌️\n";
  std::cout << "shoot! ";
  std::cin >> user;

 if (user ==  computer){
   std::cout << "It's a tie\n";
 }
 else if (user == 1){
   if (computer == 2){
     std::cout << "Computer wins\n";
   }
   if (computer == 3){
     std::cout << "You win\n";
   }
 }
 else if (user == 2){
   if (computer == 1){
     std::cout << "You win\n";
   }
   if (computer == 3){
     std::cout << "Computer wins\n";
   }
 }
 else if (user == 3){
   if (computer == 1){
     std::cout << "You win\n";
   }
   if (computer == 2){
     std::cout << "Computer wins\n";
   } 
 }

}
