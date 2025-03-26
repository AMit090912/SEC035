//1.Calculate factorial of a number :
function factorial(n){
    var result = 1;
    for(var i=1; i<=n; i++){
        result = result*i;
    }
    return result;
}
console.log(factorial(5));


//2. Swap two numbers:
console.log("Swapping to two numbers")
function swap(a,b){
    var temp = a;
    a = b;
    b =temp;
    return[a,b];
}
console.log(swap(15,18));


//3. Check if the number is odd and even:
function checkOddEven(num){
    if(num % 2 == 0){
        console.log(num + " is Even");
    }else{
        console.log(num + " is Odd");
    }
}
checkOddEven(12);
checkOddEven(7);


// 4.Print largest of two numbers:
function findLargest(a, b){
    if(a>b){
        return a;
    }else{
        return b;
    }
}
console.log(findLargest(15,12));

//5.Create a calculator in javascript:
function calculator(num1, num2, operator){
    switch(operator){
        case '+':
            return num1 + num2;
        case '-':
            return num1 - num2;
        case '*':
            return num1 * num2;
        case '/':
            return num2 !== 0 ? num1/num2 : "Cannot divide by Zero";
        default:
            return "Invalid Operator";
        
    }
}
console.log(calculator(5,7, '+'));
console.log(calculator(12,8, '-'));
console.log(calculator(4,16, '*'));
console.log(calculator(2,18, '/'));

//6. Print multiplication table of a given number:
console.log("Multiplication Table")
function table(a){
    for(var i=1;i<=10;i++){
        console.log(a+"*"+i+"="+a*i);
    }
}
table(7);

