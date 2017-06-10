import {Component, OnInit} from '@angular/core';
import {Subscription} from 'rxjs/Subscription';
import {CompIntrxnService} from '../comp-intrxn.service';
import {VisitorInfo} from '../visitor-info';

@Component({
  selector: 'app-greeting-comp',
  templateUrl: './greeting-comp.component.html',
  styleUrls: ['./greeting-comp.component.css'],
  providers: [CompIntrxnService, VisitorInfo]
})

/* Form view controller */
export class GreetingCompComponent implements OnInit {
  visitor_name: string;
  subscription: Subscription;

  handle_notification(visitor: VisitorInfo) {
    this.visitor_name = visitor.visitor_name;
  };

  /* Instantiate CompIntrxmService and inject instance to child via providers*/
  constructor(private intrxnService: CompIntrxnService) {
    this.subscription = intrxnService.form_observable$.subscribe(
      observable_visitor => {
        this.handle_notification(observable_visitor);
      });
  }

  ngOnInit() {
    this.visitor_name = 'visitor_name_ngOnInit';
  }

  /*used for diagnostic during development*/
  get diagnostic() {
    return JSON.stringify(this.visitor_name);
  }

}
