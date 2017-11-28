import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-algo-data-builder',
  templateUrl: './algo-data-builder.component.html',
  styleUrls: ['./algo-data-builder.component.css']
})
export class AlgoDataBuilderComponent implements OnInit {
  selectedFile: any;

  upload() {
    console.log('inside update ' + this.selectedFile);
  }

  constructor() { }

  ngOnInit() {
  }

}
