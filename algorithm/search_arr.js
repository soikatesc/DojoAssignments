function binarySearch(arr,key){
	var low = 0;
	var high = arr.length - 1; 

	while(low<=high){
		middle = Math.ceil((low+high)/2)
		// console.log(middle)
		if (key == arr[middle]){
			return middle;
		}
		else if(key < arr[middle]){ //search in the right half
			high = middle - 1
		}
		else if(key > arr[middle]){
			low = middle + 1
		}
	}

	return -1;
	
}

arr = [1,2,3,4,5]
console.log(binarySearch(arr,1))



