import {Injectable} from '@angular/core';
import {Subject} from 'rxjs/Subject';
import {VisitorInfo} from './visitor-info';

@Injectable()
export class CompIntrxnService {

  /* Observabke string source */
  private form_subject = new Subject<VisitorInfo>();

  /* dollar_sign$ indicates variable is of type stream*/
  form_observable$ = this.form_subject.asObservable();

  constructor() {
  }

  notify(visitor: VisitorInfo) {
    /* observer send the next notification */
    this.form_subject.next(visitor);
  }
}
