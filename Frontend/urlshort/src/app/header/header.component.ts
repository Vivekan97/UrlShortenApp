import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { AuthService } from '../_services/auth.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  activeUser!:Observable<boolean>;
  constructor(private auth:AuthService) {
    this.activeUser = this.auth.userStatus;
   }

  ngOnInit(): void {
  }

  logout(){
    this.auth.logOut();
  }
}
