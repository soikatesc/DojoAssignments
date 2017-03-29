

function numbersOnly(arr){
    var newarray=[];
    for (var i=0;i<arr.length;i++){
      if(typeof arr[i]== "number"){
        newarray.push(arr[i]);
      }
    }
  
  console.log(newarray);
  
  return newarray;
}

var arr1=numbersOnly([1,-3, "orange", 0.5]);