import { TestBed } from '@angular/core/testing';
import { UrlShortService } from './url-short.service';
import { HttpClient, HttpClientModule } from '@angular/common/http';

describe('UrlShortService', () => {
  let service: UrlShortService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientModule],
      providers: [HttpClient]
    });
    service = TestBed.inject(UrlShortService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
