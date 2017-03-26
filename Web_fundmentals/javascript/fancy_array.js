
function fancyArray(arr,symbol,reversed){
  
  if(!reversed){
    for(var i=0;i<arr.length;i++){
      console.log(i+" "+ symbol+" "+arr[i]);
    }
  }
  
  if(reversed==true){
    for(var i=arr.length-1;i>=0;i--){
      console.log(i+" "+ symbol+" "+arr[i]);
    }
    
  }
}

var arr=[ "James", "Jill", "Jane", "Jack" ];
fancyArray(arr,"-->");
fancyArray(arr,"-->",true);