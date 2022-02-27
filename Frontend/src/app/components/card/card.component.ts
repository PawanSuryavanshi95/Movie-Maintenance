import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Movie } from '../../Movie';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.css']
})
export class CardComponent implements OnInit {

  @Input() movie: Movie;

  @Output() likeMovie: EventEmitter<Movie> = new EventEmitter();

  @Output() dislikeMovie: EventEmitter<Movie> = new EventEmitter();

  constructor(){ }

  ngOnInit(): void {
  }

  likeHandler(movie: Movie){
    this.likeMovie.emit(movie);
  }

  dislikeHandler(movie: Movie){
    this.dislikeMovie.emit(movie);
  }

}
