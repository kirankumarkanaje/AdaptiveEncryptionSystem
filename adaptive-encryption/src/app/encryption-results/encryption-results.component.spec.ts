import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EncryptionResultsComponent } from './encryption-results.component';

describe('EncryptionResultsComponent', () => {
  let component: EncryptionResultsComponent;
  let fixture: ComponentFixture<EncryptionResultsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EncryptionResultsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EncryptionResultsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
