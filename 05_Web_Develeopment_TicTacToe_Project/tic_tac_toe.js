// These are all of the squares within the tic tac toe table
var boxone = document.querySelector("#b1");
var boxtwo = document.querySelector("#b2");
var boxthree = document.querySelector("#b3");
var boxfour = document.querySelector("#b4");
var boxfive = document.querySelector("#b5");
var boxsix = document.querySelector("#b6");
var boxseven = document.querySelector("#b7");
var boxeight = document.querySelector("#b8");
var boxnine = document.querySelector("#b9");

// These are the victory conditions
var firstRow = [boxone,boxtwo,boxthree];
var secondRow = [boxfour,boxfive,boxsix];
var thirdRow = [boxseven,boxeight,boxnine];

var downFirst = [boxone,boxfour,boxseven];
var downSecond = [boxtwo,boxfive,boxeight];
var downThird = [boxthree,boxsix,boxnine];

var crossOne = [boxone,boxfive,boxnine];
var crossTwo = [boxthree,boxfive,boxseven];

var everyVict = [firstRow,secondRow,thirdRow,downFirst,downSecond,downThird,crossOne,crossTwo];

function victCheck(){

    for (item of everyVict){
    function checkVictory(x,y,z){
        if (x.textContent === "X" && y.textContent === "X" && z.textContent ==="X"){
            clearBoard();
            alert("player X has won!");
        }else if (x.textContent === "O" && y.textContent === "O" && z.textContent ==="O"){
            clearBoard();
            alert("player O has won!");
        }
    }
    checkVictory(item[0],item[1],item[2]);
    }
}

// This is the display for the current player (X or O)
var playerTurnH2 = document.querySelector("#currentplayer");

// This is used to keep track of whose turn it is
var markValue = 2;
function mark(){
    if (markValue % 2 == 0){
        markValue += 1;
        playerTurnH2.textContent = "It's player 2's turn (O)";
        return "X"
    }else{
        markValue += 1;
        playerTurnH2.textContent = "It's player 1's turn (X)";
        return "O"
    }
}

// The first is the selection of the reset button 
// The second is used later on to reset all the boxes if clicked, this includes every box
var resBut = document.querySelector("#reset");
var allBox = document.getElementsByTagName("td");

///
// This is the reset button code to clear the board and replace the box values with empty strings
function clearBoard(){
    for (var i = 0; i < allBox.length; i++){
        allBox[i].textContent = " ";
    }
}

resBut.addEventListener("mouseover",function(){
    resBut.style.backgroundColor = "green";
    resBut.addEventListener("click",function(){
        clearBoard();
    })
})

function resout(boxnum){
    boxnum.style.backgroundColor = "#d4d4d4";
}

resBut.addEventListener("mouseout",function(){
    resout(resBut);
})
///

// for every box this adds event listeners for marking the boxes and styling them
var everyBox = [boxone,boxtwo,boxthree,boxfour,boxfive,boxsix,boxseven,boxeight,boxnine]
for (item of everyBox){

    function mouseOver(boxnum){
        boxnum.addEventListener("mouseover",function(){
        boxnum.style.backgroundColor = "green";
        boxnum.addEventListener("click",function(){
            if (boxnum.textContent === " "){
                boxnum.textContent = mark();
            }
            victCheck();
        })
    })
    }

    function mouseOut(boxnum){
        boxnum.addEventListener("mouseout",function(){
        boxnum.style.backgroundColor = "#d4d4d4";
        })
    }

    mouseOver(item);
    mouseOut(item);
}
