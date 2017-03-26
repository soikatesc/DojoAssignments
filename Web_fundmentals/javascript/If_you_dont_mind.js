var HOUR = 8;
var MINUTE = 40;
var PERIOD = "PM";

if (PERIOD=="AM"){
    if(HOUR==8 && MINUTE>=50){
      console.log("It's almost",HOUR+1,"in the morning");
    }
  
    if(HOUR==8 && MINUTE>30){
      console.log("It's almost", HOUR+1,"in the morning");
    }
  
     if(HOUR==8 && MINUTE<30){
      console.log("It's just after the", HOUR,"in the morning");
    }
  
}

if (PERIOD=="PM"){
    if(HOUR==8 && MINUTE>=50){
      console.log("It's almost",HOUR+1,"in the evening");
    }
  
    if(HOUR==8 && MINUTE>30){
      console.log("It's almost", HOUR+1,"in the evening");
    }
  
     if(HOUR==8 && MINUTE<30){
      console.log("It's just after the", HOUR,"in the evening");
    }
  
}