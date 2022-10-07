import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class RootService {

  apiBaseUrl:string = environment.apiUrl;

  constructor() { }

  getBaseUrl():string{
    return this.apiBaseUrl;
  }
}
