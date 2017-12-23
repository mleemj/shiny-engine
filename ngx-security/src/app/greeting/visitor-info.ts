export class VisitorInfo {
  visitor_name: string;
  constructor() {
    this.visitor_name = '';
  }
  get name(){
    return JSON.stringify(this.visitor_name);
  }
  set name(visitorName){
    this.visitor_name = visitorName;
  }
}
