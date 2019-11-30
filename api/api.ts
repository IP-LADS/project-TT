// tslint:disable
/**
 * Project TT
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


import * as globalImportUrl from 'url';
import { Configuration } from './configuration';
import globalAxios, { AxiosPromise, AxiosInstance } from 'axios';
// Some imports not used depending on template conditions
// @ts-ignore
import { BASE_PATH, COLLECTION_FORMATS, RequestArgs, BaseAPI, RequiredError } from './base';

/**
 * 
 * @export
 * @interface Location
 */
export interface Location {
    /**
     * 
     * @type {number}
     * @memberof Location
     */
    latitude?: number;
    /**
     * 
     * @type {number}
     * @memberof Location
     */
    longitude?: number;
}
/**
 * 
 * @export
 * @interface Metadata
 */
export interface Metadata {
    /**
     * 
     * @type {Array<Source>}
     * @memberof Metadata
     */
    sources?: Array<Source>;
}
/**
 * 
 * @export
 * @interface ModelError
 */
export interface ModelError {
    /**
     * 
     * @type {number}
     * @memberof ModelError
     */
    code: number;
    /**
     * 
     * @type {string}
     * @memberof ModelError
     */
    message: string;
}
/**
 * 
 * @export
 * @interface SearchCriteria
 */
export interface SearchCriteria {
    /**
     * 
     * @type {Location}
     * @memberof SearchCriteria
     */
    location?: Location;
    /**
     * 
     * @type {SearchCriteriaTimeframe}
     * @memberof SearchCriteria
     */
    timeframe?: SearchCriteriaTimeframe;
    /**
     * 
     * @type {Array<number>}
     * @memberof SearchCriteria
     */
    sources?: Array<number>;
}
/**
 * 
 * @export
 * @interface SearchCriteriaTimeframe
 */
export interface SearchCriteriaTimeframe {
    /**
     * 
     * @type {string}
     * @memberof SearchCriteriaTimeframe
     */
    dateFrom?: string;
    /**
     * 
     * @type {string}
     * @memberof SearchCriteriaTimeframe
     */
    dateTo?: string;
}
/**
 * 
 * @export
 * @interface SearchResult
 */
export interface SearchResult {
    /**
     * 
     * @type {string}
     * @memberof SearchResult
     */
    locationName?: string;
    /**
     * 
     * @type {Location}
     * @memberof SearchResult
     */
    location?: Location;
    /**
     * 
     * @type {number}
     * @memberof SearchResult
     */
    score?: number;
}
/**
 * 
 * @export
 * @interface Source
 */
export interface Source {
    /**
     * 
     * @type {number}
     * @memberof Source
     */
    id?: number;
    /**
     * 
     * @type {string}
     * @memberof Source
     */
    name?: string;
    /**
     * 
     * @type {string}
     * @memberof Source
     */
    displayName?: string;
}

/**
 * MetadataApi - axios parameter creator
 * @export
 */
export const MetadataApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary Get necessary search metadata
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getMetadata(options: any = {}): RequestArgs {
            const localVarPath = `/metadata`;
            const localVarUrlObj = globalImportUrl.parse(localVarPath, true);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }
            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;


    
            localVarUrlObj.query = {...localVarUrlObj.query, ...localVarQueryParameter, ...options.query};
            // fix override query string Detail: https://stackoverflow.com/a/7517673/1077943
            delete localVarUrlObj.search;
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...options.headers};

            return {
                url: globalImportUrl.format(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * MetadataApi - functional programming interface
 * @export
 */
export const MetadataApiFp = function(configuration?: Configuration) {
    return {
        /**
         * 
         * @summary Get necessary search metadata
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getMetadata(options?: any): (axios?: AxiosInstance, basePath?: string) => AxiosPromise<Metadata> {
            const localVarAxiosArgs = MetadataApiAxiosParamCreator(configuration).getMetadata(options);
            return (axios: AxiosInstance = globalAxios, basePath: string = BASE_PATH) => {
                const axiosRequestArgs = {...localVarAxiosArgs.options, url: basePath + localVarAxiosArgs.url};
                return axios.request(axiosRequestArgs);
            };
        },
    }
};

/**
 * MetadataApi - factory interface
 * @export
 */
export const MetadataApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    return {
        /**
         * 
         * @summary Get necessary search metadata
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getMetadata(options?: any) {
            return MetadataApiFp(configuration).getMetadata(options)(axios, basePath);
        },
    };
};

/**
 * MetadataApi - object-oriented interface
 * @export
 * @class MetadataApi
 * @extends {BaseAPI}
 */
export class MetadataApi extends BaseAPI {
    /**
     * 
     * @summary Get necessary search metadata
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof MetadataApi
     */
    public getMetadata(options?: any) {
        return MetadataApiFp(this.configuration).getMetadata(options)(this.axios, this.basePath);
    }

}


/**
 * SearchApi - axios parameter creator
 * @export
 */
export const SearchApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary Request to search over criteria
         * @param {SearchCriteria} [searchCriteria] Search criteria
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        search(searchCriteria?: SearchCriteria, options: any = {}): RequestArgs {
            const localVarPath = `/search`;
            const localVarUrlObj = globalImportUrl.parse(localVarPath, true);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }
            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;


    
            localVarHeaderParameter['Content-Type'] = 'application/json';

            localVarUrlObj.query = {...localVarUrlObj.query, ...localVarQueryParameter, ...options.query};
            // fix override query string Detail: https://stackoverflow.com/a/7517673/1077943
            delete localVarUrlObj.search;
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...options.headers};
            const needsSerialization = (typeof searchCriteria !== "string") || localVarRequestOptions.headers['Content-Type'] === 'application/json';
            localVarRequestOptions.data =  needsSerialization ? JSON.stringify(searchCriteria !== undefined ? searchCriteria : {}) : (searchCriteria || "");

            return {
                url: globalImportUrl.format(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * SearchApi - functional programming interface
 * @export
 */
export const SearchApiFp = function(configuration?: Configuration) {
    return {
        /**
         * 
         * @summary Request to search over criteria
         * @param {SearchCriteria} [searchCriteria] Search criteria
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        search(searchCriteria?: SearchCriteria, options?: any): (axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<SearchResult>> {
            const localVarAxiosArgs = SearchApiAxiosParamCreator(configuration).search(searchCriteria, options);
            return (axios: AxiosInstance = globalAxios, basePath: string = BASE_PATH) => {
                const axiosRequestArgs = {...localVarAxiosArgs.options, url: basePath + localVarAxiosArgs.url};
                return axios.request(axiosRequestArgs);
            };
        },
    }
};

/**
 * SearchApi - factory interface
 * @export
 */
export const SearchApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    return {
        /**
         * 
         * @summary Request to search over criteria
         * @param {SearchCriteria} [searchCriteria] Search criteria
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        search(searchCriteria?: SearchCriteria, options?: any) {
            return SearchApiFp(configuration).search(searchCriteria, options)(axios, basePath);
        },
    };
};

/**
 * SearchApi - object-oriented interface
 * @export
 * @class SearchApi
 * @extends {BaseAPI}
 */
export class SearchApi extends BaseAPI {
    /**
     * 
     * @summary Request to search over criteria
     * @param {SearchCriteria} [searchCriteria] Search criteria
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof SearchApi
     */
    public search(searchCriteria?: SearchCriteria, options?: any) {
        return SearchApiFp(this.configuration).search(searchCriteria, options)(this.axios, this.basePath);
    }

}


