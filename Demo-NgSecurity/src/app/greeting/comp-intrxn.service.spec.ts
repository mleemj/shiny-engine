/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { CompIntrxnService } from './comp-intrxn.service';

describe('CompIntrxnService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [CompIntrxnService]
    });
  });

  it('should ...', inject([CompIntrxnService], (service: CompIntrxnService) => {
    expect(service).toBeTruthy();
  }));
});
