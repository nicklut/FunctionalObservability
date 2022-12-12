%% Air transportation network of the domestic flights in the United States
% Loads data acquired from the TranStats database (Ref [2]). To reduce the
% dimensionality of the problem, only flights (edges) with more than 30
% people travelling from one city to another are considered. Cities (nodes)
% that do not have an influx and outflux of 30 people/day are excluded from
% the air transportation network. Thus, the US air transportation network
% is described by the connections between 81 cities.
%load airnet.mat
%  Adj         -    Adjacency matrix describing the US air transp. network
%                   (note that A(i,j) > 0 if i->j, differently from the
%                    convention adopted in Ref. [1] where A(i,j)>0 if j->i)
%  N           -    Number of cities (nodes) considered in Adj
%  P           -    Population per city (node)
%  city_coord  -    City (node) geographical coordinates 
NUM_AIRLINES = 3;
P = readmatrix('populations.txt');
lufthansa_airline = readmatrix('lufthansa_new.txt')';
british_airline = readmatrix('british_new.txt')'; 
france_airline = readmatrix('france_new.txt')';
city_coord = readmatrix('coordinates.txt');
Adj = sparse(readmatrix('adj_new.txt'));

%save('airnet.mat', 'P', '-append'); % WILL BE USED LATER TO REPLACE CUR P
save('airnet.mat', 'P', '-append');
save('airnet.mat', 'lufthansa_airline', '-append');
save('airnet.mat', 'british_airline', '-append');
save('airnet.mat', 'france_airline', '-append');
save('airnet.mat', 'Adj', '-append');
save('airnet.mat', 'city_coord', '-append');
%save('airnet.mat',



%save('airnet.mat','airline_1','-append');
%save('airnet.mat','airline_2','-append');
%save('airnet.mat','airline_3','-append');


%save('airnet.mat','air_1','-append');
%save('airnet.mat','air_2','-append');
%save('airnet.mat','air_2','-append');