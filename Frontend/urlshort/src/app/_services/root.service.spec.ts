import { HttpClientTestingModule } from '@angular/common/http/testing';
import { TestBed } from '@angular/core/testing';

import { RootService } from './root.service';

describe('RootService', () => {
  let service: RootService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports:[HttpClientTestingModule]
    });
    service = TestBed.inject(RootService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
