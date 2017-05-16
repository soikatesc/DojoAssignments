//stack constractor function

function Stack(){
	this.dataStore = [];
	this.top = 0;
	this.push = push;
	this.pop = pop;
	this.contains = contains;
	this.peek = peek;
	this.length = length;
	this.clear = clear;
	this.isEmpty = isEmpty;
}

function push(element){
	this.dataStore[this.top++] = element
}

function pop(){
	return this.dataStore[--this.top]
}

function contains(element){
	for(var i=1;i<=s.length();i++){
		if(s.dataStore[this.top-i] == element){
			return true;
		}
	}
	return false;
}

function peek(){
	return this.dataStore[this.top-1]
}

function length(){
	return this.top;
}

function clear(){
	return this.top = 0
}

function isEmpty(){
	if(this.top == 0){
		return true
	}
	return false;
}



var s = new Stack()
s.push(3)
s.push(2)

console.log(s.contains(2))
console.log(s.isEmpty())

