//first in first out

function SLNode(value){
	this.val = value;
	this.next = null;
}

// function LinkedList(){
// 	this.head = null;
// }

function SLQueue(){
	this.head = null;
	this.tail = null;
}

SLQueue.prototype.enqueue = function(val){
	var new_node = new SLNode(val)
	if(this.head == null){
		this.head = new_node
	}
}


var que = new SLQueue()
que.enqueue(3)
console.log(que)



