var counter = 1;
var limit = 10;
function addInput(divName){
     if (counter == limit)  {
          alert("No puede agregar mas de 10 actividades");
     }
     else {
          var newdiv = document.createElement('div');
          newdiv.id = "actividades";
          newdiv.innerHTML = "Actividad " + counter + " <br><input type='text' name='nombreActividad'>";
          
          document.getElementById(divName).appendChild(newdiv);
          counter++;
     }
}
