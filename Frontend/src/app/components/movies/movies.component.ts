import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Movie } from '../../Movie';

@Component({
  selector: 'app-movies',
  templateUrl: './movies.component.html',
  styleUrls: ['./movies.component.css']
})
export class MoviesComponent implements OnInit {

  readonly ROOT_URL = 'http://127.0.0.1:8000/api';

  movies:Movie[];

  sort: string;

  constructor(private http: HttpClient) {
    this.movies = [
      {
        id:'1',
        name:'No Time to Die',
        desc:'007',
        like:20,
        num_actors:40,
        release_date:'01-03-2021',
      },
      {
        id:'2',
        name:'Tenet',
        desc:'reverse',
        like:24,
        num_actors:40,
        release_date:'01-03-2021',
      },
      {
        id:'3',
        name:'Doctor Sleep',
        desc:'Shine',
        like:34,
        num_actors:40,
        release_date:'01-03-2021',
      },
    ];
    this.sort = "name";

    this.getMovies();

  }

  ngOnInit(): void {
  }

  getMovies(){
    let url = this.ROOT_URL+'/movie-list/' + this.sort + '/';

    this.http.get<Movie[]>(url).subscribe((data)=>{
      this.movies = data;
    });
  }

  likeHandler(movie:Movie, i:number){
    let url = this.ROOT_URL+'/movie-update/';
    this.http.post(url, {id:movie.id, like:i}).subscribe(data => {
      this.movies.forEach(movie2=>{
        if(movie.id===movie2.id) movie2.like = movie2.like + i;
      })
      console.log(this.movies);
    });
  }

  setSort(val:string){
    this.sort = val;
    this.getMovies();
  }

  numSequence(n: number): Array<number> {
    n = Math.floor(n);
    return Array(n);
  }

}
