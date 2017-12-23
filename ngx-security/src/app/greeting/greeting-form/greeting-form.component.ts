import {Component, OnInit} from '@angular/core';

import {VisitorInfo} from '../visitor-info';
import {CompIntrxnService} from '../comp-intrxn.service';

@Component({
  selector: 'app-greeting-form',
  templateUrl: './greeting-form.component.html',
  styleUrls: ['./greeting-form.component.css']
})
export class GreetingFormComponent implements OnInit {
  visitor: VisitorInfo;
  communication_svc: CompIntrxnService;

  constructor(serviceProviderByParent: CompIntrxnService, visitor_info: VisitorInfo) {
    this.communication_svc = serviceProviderByParent;
    this.visitor = visitor_info;
  }

  ngOnInit() {
  }
  onSubmit() {
    this.communication_svc.notify(this.visitor);
  }
  /*used for diagnostic during development*/
  get dx_form() {
    return JSON.stringify(this.visitor.visitor_name);
  }
}
