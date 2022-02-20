//p5.js script
class Grid{
  
  constructor(size, canvas_size){
    this.length=(size-1)/2;
    this.cell_length=canvas_size/size;
    
    //Creates the grid
    this.grid=new Array(size);
    for (let i = 0; i < size; i++) {
      this.grid[i] = new Array(size);
    }
    
  }
  
  //recieves array
  modgrid(xy, n){ 
    x = xy[0];
    y = xy[1];
    this.grid[this.length-y][x+this.length]=n;
  }
  
  //recieves grid
  grid_to_array(x, y){
    // console.log(x, y)
    return this.grid[this.length-y][x+this.length]
  }
  
  //transforms grid to array
  array_to_grid(x, y){
    return [this.length-y,x-this.length]
  }    
  
  //recieves grid coords
  nextcell(x, y){
    if(abs(x)>=abs(y)){
      if (x<=0){
        if (this.grid_to_array(x+1, y)==undefined){
          return [x+1, y];
        }else {
          return [x, y-1]
        }
      }else{
        if (this.grid_to_array(x-1, y)==undefined){
          return [x-1, y];
        }else {
          if(x==-y){
            return [x+1, y]
            
          }else{
            return [x, y+1]
          }
        }
      }
    }else{
      if (y<=0){
        if (this.grid_to_array(x, y+1)==undefined){
          return [x, y+1];
        }else {
          return [x+1, y]
        }
      }else{
        if (this.grid_to_array(x, y-1)==undefined){
          return [x, y-1];
        }else {
          return [x-1, y];
        }
      }
    }
  }
  
  fillgrid(){
    let counter=1;
    let x=0;
    let y=0;
    for (let i = 0; i < this.grid.length**2; i++) {
      this.modgrid([x, y], counter);
      let xy=this.nextcell(x, y);
      x=xy[0];
      y=xy[1];
      counter++;
    }
  }  
}
let face;
let n_;//has to be odd
let x,y;

function setup() {
  const size_length = 500;
  createCanvas(size_length, size_length);
  background(0);
  x = width/2;
  y = height/2;
  n_=7
  face = new Grid(n_, size_length);
  face.fillgrid();

}

function draw() {

  textSize(40);
  // textAlign(CENTER, CENTER);
  fill(255);
  let s = 70;
  for (let i=0; i<n_; i++){
    for (let j=0; j<n_; j++){
      text((face.grid[i][j]), i*s, j*s);
    }
  }
  noLoop();
}
