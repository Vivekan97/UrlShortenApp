import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ShortUrlResponse } from '../_models/model';
import { RootService } from './root.service';


@Injectable({
  providedIn: 'root'
})
export class UrlShortService {

  baseUrl!:string;

  constructor(private root:RootService, private http: HttpClient) { 
    this.baseUrl = root.getBaseUrl();
  }

  getShortenedUrl(url:string):Observable<ShortUrlResponse> {
    let shorterUrl:string = this.baseUrl + "/short";
    const request = {
      url:url
    }
    return this.http.post<ShortUrlResponse>(shorterUrl, request);
  }

  getLongUrl(url:string):Observable<ShortUrlResponse> {
    let longUrl:string = this.baseUrl + "/long";
    const request = {
      url:url
    }
    return this.http.post<ShortUrlResponse>(longUrl, request);
  }
}
