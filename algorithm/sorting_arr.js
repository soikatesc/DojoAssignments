
function bubbleSort(arr){
	for (var k=0; k<arr.length; k++){
		for (var i = 0 ; i < arr.length ; i++ ){
			if(arr[i]>arr[i+1]){
				var temp = arr[i];
				arr[i] = arr[i+1];
				arr[i+1] = temp;
			}
		}
	}
	return arr
}

function selectionSort(arr){
	for (var i=0 ; i<arr.length; i++){
		for(var j=i; j<arr.length; j++){
			if(arr[j]<arr[i]){
				var temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}

		}
	}
	return arr
}

function insertionSort(arr){
	if (arr.length == 1){
		return arr;
	}
	else{
		for(var i=1; i<arr.length; i++){
			temp = arr[i];
			var j = i;
			while(temp<arr[j-1] && j>=1){
				arr[j] = arr[j-1];
				j--;
			}
			arr[j] = temp
		}
	}
}

function printArr(arr){
	for (var i=0;i<arr.length;i++){
		console.log(arr[i]);
	}
}

arr = []
for (var i = 0 ; i<10;i++){
	random = Math.floor((Math.random() * 10) + 1);
	arr.push(random);
}
console.log('before sorting: ')
printArr(arr)

// bubbleSort(arr)
// console.log('Bubble Sort: ')
// printArr(arr)

selectionSort(arr)
console.log('Selection Sort: ')
printArr(arr)
