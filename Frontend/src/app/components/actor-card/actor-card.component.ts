import { Component, OnInit, Input, } from '@angular/core';

import { Actor } from '../../Actor';

@Component({
  selector: 'app-actor-card',
  templateUrl: './actor-card.component.html',
  styleUrls: ['./actor-card.component.css']
})
export class ActorCardComponent implements OnInit {

  @Input() actor: Actor;

  
  constructor() { }

  ngOnInit(): void {
  }

}
