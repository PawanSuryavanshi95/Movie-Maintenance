import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-actors',
  templateUrl: './actors.component.html',
  styleUrls: ['./actors.component.css']
})
export class ActorsComponent implements OnInit {

  readonly ROOT_URL = 'http://127.0.0.1:8000/api';

  actors:any;

  constructor(private http: HttpClient) {
    let url = this.ROOT_URL+'/actor-list/';
    this.actors =  this.http.get(url);
  }

  ngOnInit(): void {
  }

  getActors(){
    let url = this.ROOT_URL+'/actor-list/';
    this.actors =  this.http.get(url);
  }

}
