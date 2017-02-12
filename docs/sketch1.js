var DEBUG = true,
    FR = 0,
    GROWTH_RATE = 0.03,
    GROWTH_ACC = -0.00005,
    MIN_GROWTH_VEL = 0.001,
    MAX_BUDS = 500,
    START_RADIUS = 5,
    MAX_RADIUS = 40,
    START_POS_X = 0,
    START_POS_Y = 0,
    ADD_EVERY = 60,
    DBGMSG = "",
    K = 0.05,
    DRAG = 0.5,
    DT = 1;

var lastAdd = 0,
    lastDraw = 0,
    buds = [],
    centrePos;



function setup() {
  createCanvas(windowWidth-50, windowHeight-50);
  lastAdd = frameCount;
  lastDraw = frameCount;

  START_POS_X = width / 2;
  START_POS_Y = height / 2;

  ellipseMode(RADIUS);

  centrePos = createVector(START_POS_X , START_POS_Y);

  let second = new Bud( START_RADIUS, centrePos.copy());
  let first = new Bud( START_RADIUS, centrePos.copy().add( START_RADIUS, 0));

  buds.push( first );
  buds.push( second );

  updateBuds(0);
  // noLoop();
}

function draw() {
  DBGMSG = ""
  background(0);
  let FR = ceil(frameRate());

  // Add new
  if( (frameCount - lastAdd) >= ADD_EVERY && buds.length <= MAX_BUDS) {
    let b = new Bud( START_RADIUS, centrePos.copy());
    buds.push(b);
    lastAdd = frameCount;
  }

  // Update buds
  let dF = frameCount - lastDraw;
  lastDraw += dF;

  // DBGMSG += "dT " + dF/FR + "\n";

  updateBuds(DT);

  // Draw buds
  for(let i  = 0; i < buds.length; i++) {
    stroke(125,0,0);
    ellipse(buds[i].pos.x, buds[i].pos.y, buds[i].rad);
    if(DEBUG) {
      stroke(255, 0, 0);
      line(buds[i].pos.x, buds[i].pos.y,
            buds[i].pos.x + buds[i].force.x,
            buds[i].pos.y + buds[i].force.y );
      stroke(0, 255, 0);
      line(buds[i].pos.x, buds[i].pos.y,
            buds[i].pos.x + buds[i].vel.x,
            buds[i].pos.y + buds[i].vel.y );
    }
  }


  if(DEBUG) {
    DBGMSG += FR + " FPS\n"
          +"X: " + (mouseX - START_POS_X)
          +" Y: " + (mouseY-START_POS_Y) + "\n"
          +buds.length + " buds" + "\n";
    displayDebugInfo();
  }
}

function mousePressed() {
  noLoop();
}

function displayDebugInfo() {

  textSize(10);
  noStroke();
  fill(255);

  text(DBGMSG, 10, 10);

}

class Bud {
  constructor(rad_, pos_) {
    this.rad = rad_;
    this.pos = pos_;
    this.force = createVector(1, -1);
    this.vel = createVector(1, 1);
    this.growth = GROWTH_RATE;
  }
}

function updateBuds(dt) {


  // Grow them
  for(let i = 0; i < buds.length; i++) {
    if(buds[i].rad < MAX_RADIUS) {
      let dGrowthVel = dt*GROWTH_ACC;
      buds[i].growth += dGrowthVel;
      if(buds[i].growth < 0) {
        buds[i].growth = 0;
      }
      buds[i].rad += MIN_GROWTH_VEL + dt*buds[i].growth;
    }
  }

  // Position them
  // Attracted to the centre of the screen
  for(let i  = buds.length-1; i >= 0; i--) {
    // console.log(i);
    // Calculate the direction of the attractive force
    let c = p5.Vector.sub(buds[i].pos, centrePos);

    let totalForce = createVector(0, 0);

    // DBGMSG += i + " ";

    if ( c.mag()>0 ) {
      // totalForce.add( c.div( sq( c.mag() ) ) );
      c.mult(-K);
      totalForce.add(c);
    }

    // Calculate touching forces
    for(let j = i+1; j < buds.length; j++) {

      let repulsion = p5.Vector.sub(buds[i].pos, buds[j].pos);

      let minDistance = buds[i].rad  + buds[j].rad;
      let dR = repulsion.mag() - ( minDistance);
      // DBGMSG += " dR: " + ceil(dR) + " ";

      if(dR < 0) {
        // DBGMSG += " |r|: " + ceil(repulsion.mag()) + " ";

        let d = abs(dR);
        let th = repulsion.heading() + PI/36;
        buds[i].pos.add( d*cos(th), d*sin(th));

        // DBGMSG += " dx: " + (d*cos(th)).toFixed(2);
        // DBGMSG += " dy: " + (d*sin(th)).toFixed(2);
      }


    } // end for j

    let velocity = buds[i].vel.copy();
    let position = buds[i].pos.copy();

    let dragForce = velocity.copy().mult(-DRAG);
    totalForce.add(dragForce);

    buds[i].force = totalForce.copy();


    let dV = totalForce.mult(dt).copy();
    velocity.add(dV);

    let dP = velocity.mult(dt).copy();
    position.add(dP);




    buds[i].vel = velocity.copy();
    buds[i].pos = position.copy();

    // DBGMSG += " |v|: " + ceil(buds[i].vel.mag());
    // DBGMSG += " v: " + ceil(buds[i].vel.x) + " " + ceil(buds[i].vel.y);
    //
    // DBGMSG += "\n";


  } // end for i

}
