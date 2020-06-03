function divideBy() {
    num1 = document.getElementById("firstNumber").value;
    num2 = document.getElementById("secondNumber").value;
    num3 = 100;
    num4 = num1 / num2 * num3
    num5 = Math.round(num4)
    document.getElementById("result").innerHTML = "is " + num5 + "%" + " compared to market";


        if ((num5 < 80) || (num5 > 120)) {
            var msg = "Proposed salary is outside of BHP salary range"
            var str = msg.fontcolor("red");
            document.getElementById("message").innerHTML = str;
            // document.getElementById("message").innerHTML = "The proposed salary is outside of the range";
        }

    console.log("the number is " + num5)
}



function consoled() {
    console.log(` written in consoled on the script.js so lets see if this works`);
}

//super
function multiplySByS() {
    num1 = document.getElementById("newNumber").value;
    console.log("the new number is the first number is salary " + num1)
    num2 = document.getElementById("newSecondNumber").value;
    console.log("the five number is the second number is super " + num2)

    num3 = num2 / 100;
    console.log(num3);
    num4 = "$" + num1 * num3;
    console.log("this is the super amount in $ " + num4);
    document.getElementById("resultf").innerHTML =  num4;
}

function consoley() {
    console.log(`i pressed the button but written in consoley`)
}


//bonus
function multiplyBy() {
    num1 = document.getElementById("nineNumber").value;
    num2 = document.getElementById("tenNumber").value;
    console.log(num2)
    num3 = num2 / 100
    console.log("the bonus is " + num3)
    document.getElementById("resultc").innerHTML = "$" + num1 * num3;
}


// yyyymmdd
function dateNew() {
    var newDate = document.getElementById("proposed_Date").value;
    console.log("this is the date " + newDate)
}

//stop page reloading (could use ajax)
// $('form').submit(function(e){
//     e.preventDefault();
//
//     return false;
// });


//
// window.onload = document.getElementById("but").addEventListener('click', multiplySByS, false);

    // document.getElementById("but").addEventListener('click', consoley, false);
    document.getElementById("mybut").addEventListener('click', multiplySByS, false);
    document.getElementById("mybut").addEventListener('click', divideBy, false);
    document.getElementById("mybut").addEventListener('click', multiplyBy, false);
    document.getElementById("proposed_Date").addEventListener('keydown', dateNew, false);