# The Unbeatable TicTacToe
<p align="center">
  <img src="https://user-images.githubusercontent.com/77154447/206404533-00ca1cf9-382b-4b86-ae8e-85686d22ce8f.jpg" alt="Tic Tac Toe" width=100%>
</p>

## 📄 Description

> A TicTacToe game built in python using tkinter package for GUI. The AI bot in the game is implemented using the Minimax AI Algorithm. The AI searches through all the possibilities (forming a game tree) to find an optimal action. The Minimax Algorithm makes this game unbeatable!

## 👨‍💻 MiniMax Algorithm
> The MiniMax algorithm is a recursive algorithm used in decision-making and game theory. It delivers an optimal move for the player, considering that the competitor is also playing optimally. This algorithm is widely used for game playing in Artificial Intelligence, such as chess, tic-tac-toe, and myriad double players games.
>
> In this algorithm two players play the game, one is called MAX and other is called MIN. Both players try to increase the chances of its wining by assuming that the opponent player plays optimally. The terminal nodes of the game tree, where the game ends, are assigned an utility value, +1 if MAX wins, -1 if MIN wins, 0 if there is a draw. 
>
> The minimax algorithm performs a depth-first search algorithm for the exploration of the complete game tree. The minimax algorithm proceeds all the way down to the terminal node of the tree, then backtrack the tree as the recursion.
>
> <br>
> <p align="center">
>   <img src="https://user-images.githubusercontent.com/77154447/206404730-0a5273d3-6ac4-47c9-b8af-e990c3d59930.jpg" alt="Minimax Game Tree" style="width: 70% ">
> </p>
> <br>

## 🎮 Game Play
<table style="width:100%">
  <tr>
    <td>Draw match</td>
    <td>Bot Wins</td>
    <td>You Win</td>
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/77154447/206404965-0dfce51b-e1b0-4426-845c-041c4c2fef9f.jpg" width=100%></td>
    <td><img src="https://user-images.githubusercontent.com/77154447/206405016-1228f1d2-de0d-419d-8c1c-942355e267c0.jpg" width=100%></td>
    <td><img src="https://user-images.githubusercontent.com/77154447/206405178-615eb5cf-ad1b-46b2-a8d7-f774d1e74f50.jpg" width=93.5%></td>
  </tr>
</table>

## 🔗 References
- https://www.javatpoint.com/mini-max-algorithm-in-ai
- https://nestedsoftware.com/2019/06/15/tic-tac-toe-with-the-minimax-algorithm-5988.123625.html
- https://people.eecs.berkeley.edu/~russell/slides/chapter05.pdf
