function Stack(){
	this.dataStore = [];
	this.top = 0;
	this.push = push;
	this.pop = pop;
	this.peek = peek;
	this.length = length;
	this.clear = clear;
}

function push(element){
	this.dataStore[this.top++] = element
}

function pop(){
	return this.dataStore[--this.top]
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



function isPalindrom(word){
	var s = new Stack();
	for(var i=0;i<word.length;i++){
		s.push(word[i])
	}
	var rword = ""

	while(s.length()>0){
		rword += s.pop()
	}
	// console.log(s)
	console.log(rword)

	if(word == rword){
		return true;
	}
	false

}

var word = "racecar"
if(isPalindrom(word)){
	console.log(word+' is palnedrome')
}else{
	console.log(word+' not palnedrome')
}



