let array = [32,54,2,7,64,888,];
let minVal = array[0];

for (let i = 1; i < array.length; i++) {
    if (array[i] < minVal) {
        minVal = array[i];
    }
}

console.log(minVal);

result = 90 / 6;
console.log(result);
Number('n')
var test = (a,b) => Number(a) == Number(b);
console.log(test('',0));
console.log(1 * "two");

var tes = (28359273).toString();
var tes2 = String(28359273);
console.log(tes == tes2);
function Cat(name){
    this.name = name;
    this.gus = "icen";
    this.legs = 4;
}
let cat = new Cat("gus"); // new for invoce construc func
console.log(cat.legs);

function Animal(name,age){
    this.name = name;
    this.age = age;

    this.eat = function(food){
        console.log(`${this.name} is eating ${food}`);
    }
    function sleep(){
        console.logs(`${this.name} is sleeping`);
    }
    this.introduce = () => {
        console.log(`hello, i'm ${this.name}`);
    }

    function Cat(name, age, color){
        Animal.call(this, name, age);
        this.color = color;
        this.meow = function(){
            console.log("Meow");
        }
        
    }
    
}




