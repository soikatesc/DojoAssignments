function Stack(){
	this.dataStore = new LinkedList();
	this.top = 0;
	this.push = push;
	// this.pop = pop;
	// this.contains = contains;
	// this.length = length;
	// this.clear = clear;
	// this.isEmpty = isEmpty;
}

function LinkedList(){
	this.head = null;
}

function Node(val){
	this.val = val;
	this.next = null;
}

function push(val){
	var new_node = new Node(val);

	if(this.dataStore.head == null){
		this.dataStore.head = new_node;
	}else{
		new_node.next = this.dataStore.head;
		this.dataStore.head = new_node;
	}

	console.log(this.dataStore.head)
}


var s = new Stack()
s.push(3)
s.push(2)
console.log(s)