import {Injectable} from '@angular/core';
import {CanActivate} from '@angular/router';
import {Http, Response} from '@angular/http';

import 'rxjs/add/operator/toPromise';

@Injectable()
export class GreetingGuard implements CanActivate {
  constructor(private http: Http) {
  }

  canActivate() {
    this.http.get('http://localhost:9000')
      .toPromise()
      .then(this.extractData)
      .catch(this.handleError);
    console.log('AuthGuard#canActivate called');
    return true;
  }


  private extractData(res: Response) {
    const body = res.json();
    console.log(body);
    return body.data || {};
  }

  private handleError(error: Response | any) {
    let errMsg: string;
    if (error instanceof Response) {
      const body = error.json() || '';
      const err = body.error || JSON.stringify(body);
      errMsg = `${error.status} - ${error.statusText || ''} ${err}`;
    } else {
      errMsg = error.message ? error.message : error.toString();
    }
    /*TODO remove*/
    console.error(errMsg);
    return Promise.reject(errMsg);
  }
}
