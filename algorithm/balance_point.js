

function balancePoint(arr){

	for(var i = 0; i <= arr.length-1; i++ ){
		// console.log(arr[i])
		var leftsum = 0
		var rightsum = 0

		for(var j=0;j<=i;j++){
			leftsum += arr[j]
		}

		for(var k=i+1;k<=arr.length-1;k++){
			rightsum += arr[k]
		}

		if (leftsum == rightsum){
			// console.log(arr[j-1])
			return arr[j-1]
		}
		// console.log(rightsum)
	}

}

arr = [1,2,3,4,10]
bpoint = balancePoint(arr)
console.log(bpoint)