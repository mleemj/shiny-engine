import {Component, OnInit} from '@angular/core';
import {Observable} from 'rxjs/Observable';

@Component({
  selector: 'app-knn-form',
  templateUrl: './knn-form.component.html',
  styleUrls: ['./knn-form.component.css']
})
export class KnnFormComponent implements OnInit {
  features: string[] = [];

  constructor() {
  }

  upload(dataFile: File) {
    console.log('inside upload');
    const uri = 'http://localhost:5000/upload';
    const fd = new FormData();
    fd.append('data', dataFile, dataFile.name);
    const upload$ = Observable.create((observer) => {
        const xhr = new XMLHttpRequest();
        xhr.responseType = 'json';
        xhr.open('POST', uri, true);
        xhr.onreadystatechange = function () {
          if (xhr.status === 200) {
            const resp = xhr.response;
            for (const prop in resp) {
              console.log('resp.$[prop] = $(resp[prop)');
              observer.next(resp[prop]);
            }
          }
        };
        xhr.send(fd);
      });

    upload$.subscribe((data) => {
      console.log('Response ' + data);
      this.features.push(data);
    });
  }

  ngOnInit() {
  }

}
