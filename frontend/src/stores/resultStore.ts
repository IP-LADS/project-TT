import { computed } from 'mobx';

export interface Result {
  rank: number;
  location: string;
  popularityScore: number;
}

export class ResultStore {
  @computed
  public get isFetchingResults() {
    return false;
  }

  @computed
  public get dummyResults(): Result[] {
    return [
      {
        rank: 1,
        location: 'London',
        popularityScore: 95,
      },
      {
        rank: 2,
        location: 'Barcelona',
        popularityScore: 93.2,
      },
      {
        rank: 3,
        location: 'Dubrovnik',
        popularityScore: 91.1,
      },
      {
        rank: 4,
        location: 'Berlin',
        popularityScore: 91.1,
      },
      {
        rank: 5,
        location: 'San Francisco',
        popularityScore: 90.2,
      },
      {
        rank: 6,
        location: 'New York',
        popularityScore: 90.1,
      },
      {
        rank: 7,
        location: 'Los Angeles',
        popularityScore: 88.2,
      },
      {
        rank: 8,
        location: 'Toronto',
        popularityScore: 84,
      },
      {
        rank: 9,
        location: 'Vancouver',
        popularityScore: 81,
      },
      {
        rank: 10,
        location: 'Singapore',
        popularityScore: 80,
      },
      {
        rank: 11,
        location: 'Tokyo',
        popularityScore: 79,
      },
      {
        rank: 12,
        location: 'Manila',
        popularityScore: 75,
      },
      {
        rank: 13,
        location: 'Bangkok',
        popularityScore: 72,
      },
      {
        rank: 14,
        location: 'Hanoi',
        popularityScore: 72,
      },
      {
        rank: 15,
        location: 'Stockholm',
        popularityScore: 72,
      },
      {
        rank: 16,
        location: 'Austin',
        popularityScore: 70,
      },{
        rank: 17,
        location: 'Maine',
        popularityScore: 69,
      },{
        rank: 18,
        location: 'Madrid',
        popularityScore: 68,
      },{
        rank: 19,
        location: 'Malaga',
        popularityScore: 66,
      },{
        rank: 20,
        location: 'Seoul',
        popularityScore: 63,
      },{
        rank: 21,
        location: 'Hong Kong',
        popularityScore: 58,
      },
    ];
  }
}
